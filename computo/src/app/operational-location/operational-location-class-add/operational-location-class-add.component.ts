import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { COMMA, ENTER } from '@angular/cdk/keycodes';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { AbstractControl, FormBuilder, FormArray, ValidatorFn, ValidationErrors, AsyncValidatorFn, Validators, FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { OperationalLocationClassType } from '../../types/operational-location';
import { Router } from '@angular/router';
import { of, map, take, startWith, filter, scan, combineLatest, forkJoin } from 'rxjs';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { MatChipInputEvent } from '@angular/material/chips';

@Component({
  selector: 'app-operational-location-class-add',
  templateUrl: './operational-location-class-add.component.html',
  styleUrls: ['./operational-location-class-add.component.css']
})
export class OperationalLocationClassAddComponent implements OnInit {

  private operationalLocationClassCollection: AngularFirestoreCollection<OperationalLocationClassType>;

  separatorKeysCodes: number[] = [ENTER, COMMA];
  operationalLocationClass$: Observable<OperationalLocationClassType[]>;
  operationalLocationClassFilter$: Observable<OperationalLocationClassType[]>;

  @ViewChild('fruitInput') fruitInput: ElementRef<HTMLInputElement>;

  form = this.formBuilder.group({
    id: ['', Validators.required, this.exists()],
    created: [new Date()],
    modified: [new Date()],
    description: ['', Validators.required],
    hierarchyScope: this.formBuilder.group({
      equipmentID: ['', Validators.required],
      equipmentLevel: ['']
    }),
    operationalLocationClass: [[]],
    predicate: ['']
  });

  get objectId() {
    const id = this.form.get('id');
    return id;
  }

  constructor(
    private store: AngularFirestore,
    private formBuilder: FormBuilder,
    private router: Router
  ) {

    this.operationalLocationClassCollection = store.collection<OperationalLocationClassType>('OperationalLocationClass');
    this.operationalLocationClass$ = this.operationalLocationClassCollection.valueChanges({ idField: 'document' });

    const operationalLocationClassObservables$ = {
      data: this.operationalLocationClass$,
      predicate: this.form.controls['predicate'].valueChanges.pipe(startWith(''))
    }

    this.operationalLocationClassFilter$ = combineLatest(operationalLocationClassObservables$).pipe(
      map(observables => observables.data.filter(data => data.id.toLowerCase().includes(observables.predicate)))
    );

  }

  ngOnInit(): void {
  }

  private exists(): AsyncValidatorFn {
    return (control: AbstractControl): Observable<ValidationErrors | null> => {
      return this.store.collection(`OperationalLocationClass`, ref => ref.where('id', "==", control.value)).valueChanges().pipe(
        take(1),
        map(res => { return res.length > 0 ? { exists: true } : null })
      )
    }
  }

  set() {
    const id = this.store.createId();
    const document: OperationalLocationClassType = this.form.value;
    this.operationalLocationClassCollection.doc(id).set(document).then(result => {
      this.router.navigate(['/operational/location/class/update/' + id]);
    })
  }

  // addClass(event: MatChipInputEvent): void {
  //   const value = (event.value || '').trim();

  //   if (value) {
  //     this.form.controls['operationalLocationClass'].value.push(value);
  //   }

  //   event.chipInput!.clear();
  //   this.form.controls['predicate'].setValue(null);
  // }

  // remove(fruit: string): void {
  //   const index = this.form.controls['operationalLocationClass'].value.indexOf(fruit);

  //   if (index >= 0) {
  //     this.form.controls['operationalLocationClass'].value.splice(index, 1);
  //   }
  // }

  // selected(event: MatAutocompleteSelectedEvent): void {
  //   this.form.controls['operationalLocationClass'].value.push(event.option.viewValue);
  //   this.fruitInput.nativeElement.value = '';
  //   this.form.controls['predicate'].setValue(null);
  // }

}
