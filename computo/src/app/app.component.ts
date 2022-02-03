import { Component } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection, CollectionReference } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { FormBuilder, Validators, AbstractControl, ValidatorFn, ValidationErrors, AsyncValidatorFn, FormControl } from '@angular/forms';

export interface EquipmentClass { ID: string; Description: string; }
export interface Equipment { id: string; description: string; }

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  title = 'computo';
  private equipmentClassCollection: AngularFirestoreCollection<EquipmentClass>;
  private equipmentCollection: AngularFirestoreCollection<Equipment>;
  public formGroup: any;

  equipment: Observable<Equipment[]>;

  constructor(private readonly store: AngularFirestore, private formBuilder: FormBuilder) {
    this.equipmentClassCollection = store.collection<EquipmentClass>('EquipmentClass');
    this.equipmentCollection = store.collection<Equipment>('Equipment');
    this.equipment = this.equipmentCollection.valueChanges({ idField: 'id' });

    this.formGroup = this.formBuilder.group({
      id: [''],
      description: [''],
      x: ['']
      // ID: ['', Validators.required, this.objectIdExists()],
      // Created: [new Date()],
      // Modified: [],
      // Description: [''],
      // HierarchyScope: [''],
      // EquipmentLevel: [''],
      // SpatialDefinition: [''],
      // EquipmentAssetMapping: [[]],
      // OperationalLocation: [[]],
      // EquipmentProperty: [[]],
      // Equipment: [[]],
      // EquipmentClassID: [[]],
      // EquipmentCapabilityTestSpecificationID: [[]]
    });
    
    

  }

  public create() {
    // const description = this.form.controls['description'] as string;

    // // Persist a document id
    const id = this.store.createId();
    this.formGroup.controls['id'] = id;
    const item: Equipment = this.formGroup.value;
    console.log(item)

    this.equipmentCollection.doc(id).set(item);
  }

  public delete(id: string) {
    // const description = this.form.controls['description'] as string;
    this.equipmentCollection.doc(id).delete();
  }

}
