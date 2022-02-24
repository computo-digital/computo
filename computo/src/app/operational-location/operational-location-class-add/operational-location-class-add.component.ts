import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { FormBuilder, Validators } from '@angular/forms';
import { OperationalLocationClassType } from '../../types/operational-location';
import { Router } from '@angular/router';

@Component({
  selector: 'app-operational-location-class-add',
  templateUrl: './operational-location-class-add.component.html',
  styleUrls: ['./operational-location-class-add.component.css']
})
export class OperationalLocationClassAddComponent implements OnInit {

  private collection: AngularFirestoreCollection<OperationalLocationClassType>;

  form = this.formBuilder.group({
    id: ['', Validators.required],
    created: [new Date()],
    modified: [new Date()],
    description: ['', Validators.required],
    hierarchyScope: this.formBuilder.group({
      equipmentID: ['', Validators.required],
      equipmentLevel: ['']
    }),
    operationalLocationClass: [[]],
    operationalLocationID: [[]],
    predicate: ['']
  });

  get objectId() {
    const id = this.form.get('id');
    return id;
  }

  constructor(
    private store: AngularFirestore,
    private formBuilder: FormBuilder,
    private router: Router
  ) {
    this.collection = this.store.collection<any>('OperationalLocationClass');
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

}
