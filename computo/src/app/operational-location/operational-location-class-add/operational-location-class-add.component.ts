import { Component, OnInit } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { AbstractControl, FormBuilder, FormArray, ValidatorFn, ValidationErrors, AsyncValidatorFn, Validators } from '@angular/forms';
import { Observable } from 'rxjs';
import { OperationalLocationClassType } from '../../types/operational-location';
import { Router } from '@angular/router';
import { of, map, take } from 'rxjs';

@Component({
  selector: 'app-operational-location-class-add',
  templateUrl: './operational-location-class-add.component.html',
  styleUrls: ['./operational-location-class-add.component.css']
})
export class OperationalLocationClassAddComponent implements OnInit {

  private collection: AngularFirestoreCollection<OperationalLocationClassType>;
  documents: Observable<OperationalLocationClassType[]>;

  form = this.formBuilder.group({
    id: ['', Validators.required, this.exist()],
    created: [new Date()],
    modified: [new Date()],
    description: [''],
    hierarchyScope: this.formBuilder.group({
      equipmentID: [''],
      equipmentElementLevel: [''],
      equipmentLevel: [''],
    }),
    operationalLocationClass: [[]]
  });

  get objectId() {
    const id = this.form.get('id');
    return id;
  };

  constructor(
    private store: AngularFirestore,
    private formBuilder: FormBuilder,
    private router: Router
  ) {
    this.collection = store.collection<OperationalLocationClassType>('OperationalLocationClass');
    this.documents = this.collection.valueChanges({ idField: 'document' });
  }

  add() {
    const id = this.store.createId();
    const document: OperationalLocationClassType = this.form.value;
    this.collection.doc(id).set(document);
    this.router.navigate(['/operational/location/class/update/' + id]);
  }

  ngOnInit(): void {
  }

  private exist(): AsyncValidatorFn {
    return (control: AbstractControl): Observable<ValidationErrors | null> => {
      return this.store.collection(`OperationalLocationClass`, ref => ref.where('id', "==", control.value)).valueChanges().pipe(
        take(1),
        map(res => {
          console.log(res);
          return res.length > 0 ? { hasKey: true } : null;
        })
      );
    };
  };

}
