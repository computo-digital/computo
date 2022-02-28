import { Component, OnInit } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { OperationalLocationClassType } from 'src/app/types/operational-location';

@Component({
  selector: 'app-operational-location-class-list',
  templateUrl: './operational-location-class-list.component.html',
  styleUrls: ['./operational-location-class-list.component.css']
})
export class OperationalLocationClassListComponent implements OnInit {

  private collection: AngularFirestoreCollection<OperationalLocationClassType>;
  documents: Observable<OperationalLocationClassType[]>;
  controls: boolean = false;
  columns: string[] = [
    'id', 
    'description',
    'hierarchyScopeEquipmentLevel',
    'hierarchyScopeEquipmentID',
    // 'operationalLocationClass',
    // 'operationalLocationID',
    // 'operationalLocationClassProperty',
    'controls'
  ];

  constructor(private readonly store: AngularFirestore) {
    this.collection = store.collection<OperationalLocationClassType>('OperationalLocationClass')
    this.documents = this.collection.valueChanges({ idField: 'document' });
  }

  ngOnInit(): void {
  }

}
