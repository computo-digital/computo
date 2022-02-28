import { Component, OnInit, Input } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { EquipmentElementLevelType } from '../../types/common';
import { AbstractControl, FormGroup, FormBuilder, FormArray, ValidatorFn, ValidationErrors, AsyncValidatorFn, Validators, FormControl } from '@angular/forms';
import { EquipmentType } from '../../types/equipment';
import { Observable, of, map, take, startWith, filter, scan, combineLatest, forkJoin } from 'rxjs';
import { MatAutocompleteSelectedEvent, MatAutocomplete } from '@angular/material/autocomplete';

@Component({
  selector: 'app-hierarchy',
  templateUrl: './hierarchy.component.html',
  styleUrls: ['./hierarchy.component.css']
})
export class HierarchyComponent implements OnInit {

  @Input() form: FormGroup;
  autocompleteForm = new FormControl();
  private equipmentCollection: AngularFirestoreCollection<EquipmentType>;
  equipment$: Observable<EquipmentType[]>;
  equipmentFilter$: Observable<EquipmentType[]>;
  equipmentElementLevelType = EquipmentElementLevelType;

  constructor(private store: AngularFirestore) {
    this.equipmentCollection = store.collection<EquipmentType>('Equipment');
    this.equipment$ = this.equipmentCollection.valueChanges({ idField: 'document' });

    const observables$ = {
      data: this.equipment$,
      predicate: this.autocompleteForm.valueChanges.pipe(startWith(''))
    }

    this.equipmentFilter$ = combineLatest(observables$).pipe(
      map(observables => observables.data.filter(data => data.id.toLowerCase().includes(observables.predicate)))
    );

  }

  ngOnInit(): void {
    this.form.statusChanges.subscribe(statue => this.patch());
  }

  set(event: MatAutocompleteSelectedEvent): void {
    const equipmentID = this.form.get('hierarchyScope.equipmentID');
    const equipmentLevel = this.form.get('hierarchyScope.equipmentLevel');
    equipmentID?.setValue(event.option.value.id);
    equipmentLevel?.setValue(event.option.value.equipmentLevel.equipmentLevel);
    // this.autocompleteForm.setValue(event.option.value.id);
  }

  patch() {
    const equipmentID = this.form.get('hierarchyScope.equipmentID');
    this.autocompleteForm.setValue(equipmentID?.value);
  }

}
