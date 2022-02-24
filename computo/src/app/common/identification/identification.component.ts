import { Component, OnInit, Input } from '@angular/core';
import { AngularFirestore } from '@angular/fire/compat/firestore';
import { AbstractControl, FormGroup, FormBuilder, ValidationErrors, AsyncValidatorFn, Validators } from '@angular/forms';
import { Observable, map, take } from 'rxjs';

@Component({
  selector: 'app-identification',
  templateUrl: './identification.component.html',
  styleUrls: ['./identification.component.css']
})
export class IdentificationComponent implements OnInit {

  @Input() form: FormGroup;
  @Input() collectionName: string;

  idForm = this.formBuilder.group({
    id: ['', Validators.required, this.exists()]
  });

  constructor(
    private store: AngularFirestore,
    private formBuilder: FormBuilder
  ) {
    this.idForm.statusChanges.subscribe(status => { this.set() });
  }

  ngOnInit(): void {
  }

  get objectId() {
    const id = this.idForm.get('id');
    return id;
  }

  private exists(): AsyncValidatorFn {
    return (control: AbstractControl): Observable<ValidationErrors | null> => {
      return this.store.collection(this.collectionName, ref => ref.where('id', "==", control.value)).valueChanges().pipe(
        take(1),
        map(res => { return res.length > 0 ? { exists: true } : null })
      )
    }
  }

  set(): void {
    if (this.idForm.controls['id'].valid) {
      const id = this.form.get('id');
      id?.setValue(this.idForm.controls['id'].value);
    }
  }
}
