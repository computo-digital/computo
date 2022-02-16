import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap, Data } from '@angular/router';
import { AngularFirestore, AngularFirestoreDocument } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { OperationalLocationClassType } from '../../types/operational-location-class';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-operational-location-class-update',
  templateUrl: './operational-location-class-update.component.html',
  styleUrls: ['./operational-location-class-update.component.css']
})
export class OperationalLocationClassUpdateComponent implements OnInit {

  public id: string | null = null;
  private document: AngularFirestoreDocument<OperationalLocationClassType>;
  public snapshot: Observable<any>;
  public form: any;
  public timestamp: any = new Date(0);

  constructor(
    private route: ActivatedRoute,
    private store: AngularFirestore,
    private formBuilder: FormBuilder
  ) {
    this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
      this.document = this.store.doc<OperationalLocationClassType>('OperationalLocationClassType/' + this.id);
      this.snapshot = this.document.snapshotChanges();

      this.form = this.formBuilder.group({
        id: [''],
        description: ['']
      });

    });

  }

  ngOnInit(): void {
    this.snapshot.subscribe(document => {
      this.form.patchValue(document.payload.data());
    })
  }

  public update() {
    this.document.update(this.form.value);
  }

}
