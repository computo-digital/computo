import { Component, OnInit } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { OperationalLocationClassType } from 'src/app/types/operational-location-class';
import { FormBuilder } from '@angular/forms';
import { HierarchyScopeType, ValueType } from '../../types/common';

@Component({
  selector: 'app-operational-location-class-add',
  templateUrl: './operational-location-class-add.component.html',
  styleUrls: ['./operational-location-class-add.component.css']
})
export class OperationalLocationClassAddComponent implements OnInit {

  private collection: AngularFirestoreCollection<OperationalLocationClassType>;
  public data: Observable<OperationalLocationClassType[]>;
  public form: any;
  public timestamp: any = new Date(0);

  constructor(
    private readonly store: AngularFirestore,
    private formBuilder: FormBuilder
    ) {
    this.collection = store.collection<OperationalLocationClassType>('OperationalLocationClassType')
    this.data = this.collection.valueChanges({ idField: 'id' });

    this.form = this.formBuilder.group({
      id: [''],
      description: [''],
      hierarchyScope: ['']
    });

  }

  ngOnInit(): void {
  }

  add() {
    // Persist a document id
    const id = this.store.createId();
    // const document: OperationalLocationClassType = { id, name };
    this.collection.doc(id).set(this.form.value);
  }

}
