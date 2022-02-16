import { Component, OnInit } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { OperationalLocationClassType } from 'src/app/types/operational-location-class';

@Component({
  selector: 'app-operational-location-class-list',
  templateUrl: './operational-location-class-list.component.html',
  styleUrls: ['./operational-location-class-list.component.css']
})
export class OperationalLocationClassListComponent implements OnInit {

  private collection: AngularFirestoreCollection<OperationalLocationClassType>;
  data: Observable<OperationalLocationClassType[]>;
  columns: string[] = [
    'id', 
    'description',
    'hierarchyScope',
    'operationalLocationClass',
    'operationalLocationID',
    'operationalLocationClassProperty'
  ];

  constructor(private readonly store: AngularFirestore) {
    this.collection = store.collection<OperationalLocationClassType>('OperationalLocationClassType')
    this.data = this.collection.valueChanges({ idField: 'id' });
  }

  ngOnInit(): void {
  }

}
