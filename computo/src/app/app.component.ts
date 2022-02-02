import { Component } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection , CollectionReference} from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';

export interface EquipmentClass { ID: string; Description: string;}
export interface Equipment { ID: string; Description: string; EquipmentClass: EquipmentClass; }

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  title = 'computo';
  private equipmentClassCollection: AngularFirestoreCollection<EquipmentClass>;
  private equipmentCollection: AngularFirestoreCollection<Equipment>;

  equipment: Observable<Equipment[]>;
  
  constructor(private readonly store: AngularFirestore) {
    this.equipmentClassCollection = store.collection<EquipmentClass>('EquipmentClass');
    this.equipmentCollection = store.collection<Equipment>('Equipment');
    this.equipment = this.equipmentCollection.valueChanges({ idField: 'ID' });

  }
  addEquipment(Description: string, EquipmentClass: EquipmentClass) {
    // Persist a document id
    const ID = this.store.createId();
    const item: Equipment = { ID, Description, EquipmentClass};
    this.equipmentCollection.doc(ID).set(item);
  }
}
