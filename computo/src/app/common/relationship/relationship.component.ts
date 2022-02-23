import { Component, OnInit, Input, ElementRef, ViewChild } from '@angular/core';
import { COMMA, ENTER } from '@angular/cdk/keycodes';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { AbstractControl, FormGroup, FormBuilder, FormArray, ValidatorFn, ValidationErrors, AsyncValidatorFn, Validators, FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { OperationalLocationClassType } from '../../types/operational-location';
import { Router } from '@angular/router';
import { of, map, take, startWith, filter, scan, combineLatest, forkJoin } from 'rxjs';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { MatChipInputEvent } from '@angular/material/chips';

@Component({
  selector: 'app-relationship',
  templateUrl: './relationship.component.html',
  styleUrls: ['./relationship.component.css']
})
export class RelationshipComponent implements OnInit {

  @Input() form: FormGroup;
  @Input() label: string;
  @Input() collectionName: string;
  @Input() relationshipName: string;
  @ViewChild('relationshipInput') relationshipInput: ElementRef<HTMLInputElement>;
  private operationalLocationClassCollection: AngularFirestoreCollection<any>;
  autocompleteForm = new FormControl();
  separatorKeysCodes: number[] = [ENTER, COMMA];
  operationalLocationClass$: Observable<any[]>;
  operationalLocationClassFilter$: Observable<any[]>;

  constructor(
    private store: AngularFirestore
  ) { }

  ngOnInit(): void {
    this.operationalLocationClassCollection = this.store.collection<any>(this.collectionName);
    this.operationalLocationClass$ = this.operationalLocationClassCollection.valueChanges({ idField: 'document' });

    const operationalLocationClassObservables$ = {
      data: this.operationalLocationClass$,
      predicate: this.autocompleteForm.valueChanges.pipe(startWith(''))
    }

    this.operationalLocationClassFilter$ = combineLatest(operationalLocationClassObservables$).pipe(
      map(observables => observables.data.filter(data => data.id.toLowerCase().includes(observables.predicate)))
    );
  }

  add(event: MatChipInputEvent): void {
    const value = (event.value || '').trim();

    if (value) {
      this.form.controls[this.relationshipName].value.push(value);
    }

    event.chipInput!.clear();
    this.autocompleteForm.setValue(null);
  }

  remove(relationship: string): void {
    const index = this.form.controls[this.relationshipName].value.indexOf(relationship);

    if (index >= 0) {
      this.form.controls[this.relationshipName].value.splice(index, 1);
    }
  }

  selected(event: MatAutocompleteSelectedEvent): void {
    this.form.controls[this.relationshipName].value.push(event.option.viewValue);
    this.relationshipInput.nativeElement.value = '';
    this.autocompleteForm.setValue('');
    
  }

}
