import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AngularFirestore, AngularFirestoreDocument, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { FormBuilder, Validators } from '@angular/forms';
import { OperationalLocationClassType, OperationalLocationPropertyType } from '../../types/operational-location';

@Component({
  selector: 'app-operational-location-class-update',
  templateUrl: './operational-location-class-update.component.html',
  styleUrls: ['./operational-location-class-update.component.css']
})
export class OperationalLocationClassUpdateComponent implements OnInit {

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
    const id = this.route.snapshot.paramMap.get('id');
    this.document = store.doc<OperationalLocationClassType>('OperationalLocationClass/' + id);
    this.document.valueChanges().subscribe(document => {
      this.form.patchValue(document as any);
      this.form.controls['id'].disable();
    })
  }

  ngOnInit(): void {
  }

  update() {
    const document: OperationalLocationClassType = this.form.value;
    document.modified = new Date();
    this.document.update(document);
  }

}
