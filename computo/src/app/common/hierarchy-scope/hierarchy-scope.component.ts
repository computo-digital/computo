import { Component, OnInit, Input} from '@angular/core';
import { EquipmentElementLevelType } from '../../types/common';
import { AbstractControl, FormGroup, FormBuilder, FormArray, ValidatorFn, ValidationErrors, AsyncValidatorFn, Validators, FormControl } from '@angular/forms';

@Component({
  selector: 'app-hierarchy-scope',
  templateUrl: './hierarchy-scope.component.html',
  styleUrls: ['./hierarchy-scope.component.css']
})
export class HierarchyScopeComponent implements OnInit {

  @Input() form: FormGroup;

  equipmentElementLevelType = EquipmentElementLevelType;

  constructor(private formBuilder: FormBuilder,) { }

  ngOnInit(): void {
  }

  set() {
  }

}
