import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { AbstractControl, FormGroup, FormBuilder, FormArray, ValidatorFn, ValidationErrors, AsyncValidatorFn, Validators, FormControl } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AngularFirestore, AngularFirestoreDocument, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { OperationalLocationClassType, OperationalLocationPropertyType } from '../../types/operational-location';
import { DataTypeType, UnitOfMeasureType } from '../../types/common';
import {  } from '@angular/material/';

@Component({
  selector: 'app-property',
  templateUrl: './property.component.html',
  styleUrls: ['./property.component.css']
})
export class PropertyComponent implements OnInit {

  @Input() label: string;
  @Input() path: string;
  @Input() collection: string;

  private document: AngularFirestoreDocument<any>;
  private property: AngularFirestoreDocument<any>;
  property$: Observable<any | undefined>;
  properties$: Observable<any[]>;
  dataTypeType = DataTypeType;
  unitOfMeasureType = UnitOfMeasureType;
  showFiller = false;
  isNew = false;

  form = this.builder.group({
    id: ['', Validators.required],
    created: [new Date()],
    modified: [new Date()],
    description: ['', Validators.required],
    value: this.builder.group({
      valueString: [''],
      dataType: [''],
      unitOfMeasure: ['']
    }),
    propertyType: [[]]
  });

  columns: string[] = [
    'id', 
    'description',
    'valueString',
    'dataType',
    'unitOfMeasure'
  ];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private store: AngularFirestore,
    private builder: FormBuilder,
  ) 
  {}

  ngOnInit(): void {
    this.document = this.store.doc<any>(this.path + '/' + this.route.snapshot.paramMap.get('id'));

    this.document.valueChanges().subscribe(document => {
      this.properties$ = this.document.collection<any>(this.collection).valueChanges({idField: 'document'});
    })
  }

  new(drawer: any){
    this.form.controls['id'].enable();
    this.form.reset();

    if(!drawer.opened){
      drawer.toggle();
    }

    this.isNew = true;
  }

  open(drawer: any, document: string) {
    const path = this.path + '/' + this.route.snapshot.paramMap.get('id') + '/' + this.collection + '/' + document;
    this.property = this.store.doc<any>(path);
    this.property.valueChanges({idField: 'document'}).subscribe(document => {
      this.form.patchValue(document as any);
      this.form.controls['id'].disable();
    })

    if(!drawer.opened){
      drawer.toggle();
    }

    this.isNew = false;
  }

  add() {
    this.document.collection<any>(this.collection).add(this.form.value);
    this.form.reset();
  }

  delete() {
    this.property.delete();
    this.form.reset();
  }

  update() {
    this.form.controls['id'].enable();
    this.property.update(this.form.value);
  }

}
