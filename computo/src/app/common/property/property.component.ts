import { Component, OnInit, Input } from '@angular/core';
import { AbstractControl, FormGroup, FormBuilder, FormArray, ValidatorFn, ValidationErrors, AsyncValidatorFn, Validators, FormControl } from '@angular/forms';

@Component({
  selector: 'app-property',
  templateUrl: './property.component.html',
  styleUrls: ['./property.component.css']
})
export class PropertyComponent implements OnInit {

  @Input() form: FormGroup;
  @Input() label: string;
  @Input() collectionName: string;
  @Input() property: string;

  constructor() { }

  ngOnInit(): void {
  }

}
