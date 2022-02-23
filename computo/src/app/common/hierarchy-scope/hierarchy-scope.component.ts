import { Component, OnInit, Input } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { EquipmentElementLevelType } from '../../types/common';
import { AbstractControl, FormGroup, FormBuilder, FormArray, ValidatorFn, ValidationErrors, AsyncValidatorFn, Validators, FormControl } from '@angular/forms';
import { EquipmentType } from '../../types/equipment';
import { Observable, of, map, take, startWith, filter, scan, combineLatest, forkJoin } from 'rxjs';
import { MatAutocompleteSelectedEvent, MatAutocomplete } from '@angular/material/autocomplete';

@Component({
  selector: 'app-hierarchy-scope',
  templateUrl: './hierarchy-scope.component.html',
  styleUrls: ['./hierarchy-scope.component.css']
})
export class HierarchyScopeComponent implements OnInit {

  @Input() form: FormGroup;

  autocompleteForm = new FormControl();

  private equipmentCollection: AngularFirestoreCollection<EquipmentType>;
  equipment$: Observable<EquipmentType[]>;
  equipmentFilter$: Observable<EquipmentType[]>;

  equipmentElementLevelType = EquipmentElementLevelType;

  constructor(private store: AngularFirestore) { 
    this.equipmentCollection = store.collection<EquipmentType>('Equipment');
    this.equipment$ = this.equipmentCollection.valueChanges({ idField: 'document' });

    const equipmentObservables$ = {
      data: this.equipment$,
      predicate: this.autocompleteForm.valueChanges.pipe(startWith(''))
    }

    this.equipmentFilter$ = combineLatest(equipmentObservables$).pipe(
      map(observables => observables.data.filter(data => data.id.toLowerCase().includes(observables.predicate)))
    );
    
  }

  ngOnInit(): void {
  }

  setEquipmentID(event: MatAutocompleteSelectedEvent): void {
    const equipmentID = this.form.get('hierarchyScope.equipmentID');
    const equipmentLevel = this.form.get('hierarchyScope.equipmentLevel');
    equipmentID?.setValue(event.option.value.id);
    equipmentLevel?.setValue(event.option.value.equipmentLevel.equipmentLevel);
    this.autocompleteForm.setValue(event.option.value.id);
  }
  
}
