import { Component, OnInit } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { OperationalLocationClassType } from 'src/app/types/operational-location-class';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-operational-location-class-add',
  templateUrl: './operational-location-class-add.component.html',
  styleUrls: ['./operational-location-class-add.component.css']
})
export class OperationalLocationClassAddComponent implements OnInit {

  private collection: AngularFirestoreCollection<OperationalLocationClassType>;
  list: Observable<OperationalLocationClassType[]>;
  form: any;

  constructor(
    private readonly store: AngularFirestore,
    private formBuilder: FormBuilder
  ) {
    this.collection = store.collection<OperationalLocationClassType>('OperationalLocationClassType');
    this.list = this.collection.valueChanges({ idField: 'id' });
    this.form = this.formBuilder.group({
      id: [''],
      created: [new Date()],
      description: [''],
      hierarchyScope: ['']
    });
  }

  ngOnInit(): void {
  }

  add() {
    // Persist a document id
    // const document: OperationalLocationClassType = { id, name };
    this.collection.doc(this.form.controls['id'].value).set(this.form.value);
  }

}
