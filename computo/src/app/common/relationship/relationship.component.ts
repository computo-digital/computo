import { Component, OnInit, Input, ElementRef, ViewChild } from '@angular/core';
import { COMMA, ENTER } from '@angular/cdk/keycodes';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { AbstractControl, FormGroup, FormBuilder, FormArray, ValidatorFn, ValidationErrors, AsyncValidatorFn, Validators, FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { OperationalLocationClassType } from '../../types/operational-location';
import { Router } from '@angular/router';
import { of, map, take, startWith, filter, scan, combineLatest, forkJoin } from 'rxjs';
import { MatAutocompleteSelectedEvent, MatAutocompleteTrigger } from '@angular/material/autocomplete';
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
  @ViewChild('autoTrigger', { read: MatAutocompleteTrigger })
  autoTrigger: MatAutocompleteTrigger;

  @ViewChild('relationshipInput') relationshipInput: ElementRef<HTMLInputElement>;
  private collection: AngularFirestoreCollection<any>;
  predicate = new FormControl();
  separator: number[] = [ENTER, COMMA];
  collection$: Observable<any[]>;
  filter$: Observable<any[]>;
  observables$: any;

  constructor(
    private store: AngularFirestore
  ) { }

  ngOnInit(): void {
    this.collection = this.store.collection<any>(this.collectionName);
    this.collection$ = this.collection.valueChanges({ idField: 'document' });

    const observables$ = {
      data: this.collection$,
      predicate: this.predicate.valueChanges.pipe(startWith(''))
    }

    this.filter$ = combineLatest(observables$).pipe(
      map(observables => observables.data.filter(data => data.id.toLowerCase().includes(observables.predicate)))
    );

    // this.form.statusChanges.subscribe(statue => this.patch());
  }

  add(event: MatChipInputEvent): void {
    const value = (event.value || '').trim();

    if (value) {
      this.form.controls[this.relationshipName].value.push(value);
    }

    event.chipInput!.clear();
    this.predicate.setValue(null);
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
    this.predicate.setValue('');
  }

  patch() {
    const relationship = this.form.get(this.relationshipName);
    this.predicate.setValue(relationship?.value);
  }


}
