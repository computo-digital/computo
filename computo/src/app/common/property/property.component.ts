import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { AbstractControl, FormGroup, FormBuilder, FormArray, ValidatorFn, ValidationErrors, AsyncValidatorFn, Validators, FormControl } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AngularFirestore, AngularFirestoreDocument, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { OperationalLocationClassType, OperationalLocationPropertyType } from '../../types/operational-location';
import { DataTypeType, UnitOfMeasureType } from '../../types/common';

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
  id : string;
  dataTypeType = DataTypeType;
  unitOfMeasureType = UnitOfMeasureType;
  showFiller = false;
  isNew = false;
  active: any | null;

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
    'valueString',
    'dataType',
    'unitOfMeasure',
    'action'
  ];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private store: AngularFirestore,
    private builder: FormBuilder,
  ) 
  {
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.id = params['id'];
      this.document = this.store.doc<any>(this.path + '/' + params['id']);
      this.document.valueChanges().subscribe(document => {
        this.properties$ = this.document.collection<any>(this.collection).valueChanges({idField: 'document'});
      })
    })
  }

  new(){
    this.form.controls['id'].enable();
    this.form.reset();
    this.isNew = true;
  }

  open(document: string) {
    console.log('open document', document);

    this.active = document

    const path = this.path + '/' + this.id + '/' + this.collection + '/' + document;
    this.property = this.store.doc<any>(path);

    this.property.valueChanges({idField: 'document'}).subscribe(document => {
      this.form.patchValue(document as any);
      this.form.controls['id'].disable();
    })
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