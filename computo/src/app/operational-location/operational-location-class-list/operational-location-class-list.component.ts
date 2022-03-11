import { Component, OnInit } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { ActivatedRoute } from '@angular/router';
import { doc } from 'firebase/firestore';
import { Observable } from 'rxjs';
import { OperationalLocationClassType } from 'src/app/types/operational-location';

@Component({
  selector: 'app-operational-location-class-list',
  templateUrl: './operational-location-class-list.component.html',
  styleUrls: ['./operational-location-class-list.component.css']
})
export class OperationalLocationClassListComponent implements OnInit {

  private collection: AngularFirestoreCollection<OperationalLocationClassType>;
  documents$: Observable<OperationalLocationClassType[]>;
  document: string;

  columns: string[] = [
    'id', 
    'description',
    'hierarchyScopeEquipmentID',
    'hierarchyScopeEquipmentLevel',
    'action'
  ];

  constructor(
    private readonly store: AngularFirestore,
    private route: ActivatedRoute
    ) {
    this.collection = store.collection<OperationalLocationClassType>('OperationalLocationClass')
    this.documents$ = this.collection.valueChanges({ idField: 'document' });
  }

  ngOnInit(): void {
  }

  open(document: string, drawer: any){
    this.document = document;
    
    if(!drawer.opened){
      drawer.toggle();
    }
  }

}
