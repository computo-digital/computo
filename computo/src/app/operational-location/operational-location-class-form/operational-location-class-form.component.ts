import { Component, OnInit } from '@angular/core';
import { AngularFirestore, AngularFirestoreDocument, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { FormBuilder, Validators } from '@angular/forms';
import { OperationalLocationClassType, OperationalLocationPropertyType } from '../../types/operational-location';
import { ActivatedRoute, Router } from '@angular/router';

export interface Item { name: string; }

@Component({
  selector: 'app-operational-location-class-form',
  templateUrl: './operational-location-class-form.component.html',
  styleUrls: ['./operational-location-class-form.component.css']
})
export class OperationalLocationClassFormComponent implements OnInit {

  private collection: AngularFirestoreCollection<OperationalLocationClassType>;
  collection$: Observable<OperationalLocationClassType[]>;
  private document: AngularFirestoreDocument<OperationalLocationClassType>;
  private property: AngularFirestoreDocument<OperationalLocationPropertyType>;
  document$: Observable<OperationalLocationClassType | undefined>;
  property$: Observable<OperationalLocationPropertyType | undefined>;
  properties$: Observable<OperationalLocationPropertyType[]>;

  form = this.builder.group({
    id: ['', Validators.required],
    created: [new Date()],
    modified: [new Date()],
    description: ['', Validators.required],
    hierarchyScope: this.builder.group({
      equipmentID: ['', Validators.required],
      equipmentLevel: ['']
    }),
    operationalLocationClass: [[]],
    operationalLocationID: [[]]
  });

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private store: AngularFirestore,
    private builder: FormBuilder,
  ) {

    if (this.route.snapshot.paramMap.get('id')){
      console.log(this.route.snapshot.paramMap.get('id'));
    }

    this.collection = store.collection<OperationalLocationClassType>('OperationalLocationClass');
    this.collection$ = this.collection.valueChanges();
    this.document = store.doc<OperationalLocationClassType>('OperationalLocationClass/1');
    this.property = store.doc<OperationalLocationPropertyType>('OperationalLocationClass/1/tasks/OYReR2oLcQBrQ5IZ7z6G');
    this.document$ = this.document.valueChanges();
    this.property$ = this.property.valueChanges();
    this.properties$ = this.document.collection<OperationalLocationPropertyType>('tasks').valueChanges();
  }

  ngOnInit(): void {
  }

  set() {
    const id = this.store.createId();
    const document: OperationalLocationClassType = this.form.value;
    this.collection.doc(id).set(document).then(result => {
      this.router.navigate(['/operational/location/class/update/' + id]);
    })
  }

  addProperty(property: OperationalLocationPropertyType) {
    this.document.collection<OperationalLocationPropertyType>('tasks').add(property);
  }

  update(document: OperationalLocationClassType) {
    this.document.update(document);
  }

}

// import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
// import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
// import { FormBuilder, Validators } from '@angular/forms';
// import { OperationalLocationClassType } from '../../types/operational-location';
// import { Router } from '@angular/router';

// @Component({
//   selector: 'app-operational-location-class-form',
//   templateUrl: './operational-location-class-form.component.html',
//   styleUrls: ['./operational-location-class-form.component.css']
// })
// export class OperationalLocationClassFormComponent implements OnInit {

//   private collection: AngularFirestoreCollection<OperationalLocationClassType>;

//   form = this.formBuilder.group({
//     id: ['', Validators.required],
//     created: [new Date()],
//     modified: [new Date()],
//     description: ['', Validators.required],
//     hierarchyScope: this.formBuilder.group({
//       equipmentID: ['', Validators.required],
//       equipmentLevel: ['']
//     }),
//     operationalLocationClass: [[]],
//     operationalLocationID: [[]]
//   });

//   get objectId() {
//     const id = this.form.get('id');
//     return id;
//   }

//   constructor(
//     private store: AngularFirestore,
//     private formBuilder: FormBuilder,
//     private router: Router
//   ) {
//     this.collection = this.store.collection<any>('OperationalLocationClass');
//   }

//   ngOnInit(): void {
//   }

//   set() {
//     const id = this.store.createId();
//     const document: OperationalLocationClassType = this.form.value;
//     this.collection.doc(id).set(document).then(result => {
//       this.router.navigate(['/operational/location/class/update/' + id]);
//     })
//   }

// }

