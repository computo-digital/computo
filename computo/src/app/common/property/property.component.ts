import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { AbstractControl, FormGroup, FormBuilder, FormArray, ValidatorFn, ValidationErrors, AsyncValidatorFn, Validators, FormControl } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AngularFirestore, AngularFirestoreDocument, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { OperationalLocationClassType, OperationalLocationPropertyType } from '../../types/operational-location';
import { DataTypeType, UnitOfMeasureType } from '../../types/common';
import { animate, state, style, transition, trigger } from '@angular/animations';

@Component({
  selector: 'app-property',
  templateUrl: './property.component.html',
  styleUrls: ['./property.component.css'],
  animations: [
    trigger('detailExpand', [
      state('collapsed', style({height: '0px', minHeight: '0'})),
      state('expanded', style({height: '*'})),
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],
})
export class PropertyComponent implements OnInit {

  @Input() label: string;
  @Input() path: string;
  @Input() collection: string;

  private document: AngularFirestoreDocument<any>;
  private property: AngularFirestoreDocument<any>;
  property$: Observable<any | undefined>;
  properties$: Observable<any[]>;
  id : string;
  dataTypeType = DataTypeType;
  unitOfMeasureType = UnitOfMeasureType;
  showFiller = false;
  isNew = false;
  expandedElement: any | null;


  dataSource = ELEMENT_DATA;
  // columnsToDisplay = ['name', 'weight', 'symbol', 'position'];


  form = this.builder.group({
    id: ['', Validators.required],
    created: [new Date()],
    modified: [new Date()],
    description: ['', Validators.required],
    value: this.builder.group({
      valueString: [''],
      dataType: [''],
      unitOfMeasure: ['']
    }),
    propertyType: [[]]
  });

  columns: string[] = [
    'id', 
    'description',
    'valueString',
    'dataType',
    'unitOfMeasure',
  ];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private store: AngularFirestore,
    private builder: FormBuilder,
  ) 
  {
    this.route.params.subscribe(params => {
      this.id = params['id'];
      this.document = this.store.doc<any>(this.path + '/' + params['id']);
      this.document.valueChanges().subscribe(document => {
        this.properties$ = this.document.collection<any>(this.collection).valueChanges({idField: 'document'});
      })
    })

  }

  ngOnInit(): void {
  }

  new(){
    this.form.controls['id'].enable();
    this.form.reset();

    this.isNew = true;
  }

  open(document: string) {
    const path = this.path + '/' + this.id + '/' + this.collection + '/' + document;
    this.property = this.store.doc<any>(path);

    this.property.valueChanges({idField: 'document'}).subscribe(document => {
      this.form.patchValue(document as any);
      this.form.controls['id'].disable();
    })

    this.isNew = false;
  }

  add() {
    this.document.collection<any>(this.collection).add(this.form.value);
    this.form.reset();
  }

  delete() {
    this.property.delete();
    this.form.reset();
  }

  update() {
    this.form.controls['id'].enable();
    this.property.update(this.form.value);
  }


}




export interface PeriodicElement {
  name: string;
  position: number;
  weight: number;
  symbol: string;
  description: string;
}

const ELEMENT_DATA: PeriodicElement[] = [
  {
    position: 1,
    name: 'Hydrogen',
    weight: 1.0079,
    symbol: 'H',
    description: `Hydrogen is a chemical element with symbol H and atomic number 1. With a standard
        atomic weight of 1.008, hydrogen is the lightest element on the periodic table.`,
  },
  {
    position: 2,
    name: 'Helium',
    weight: 4.0026,
    symbol: 'He',
    description: `Helium is a chemical element with symbol He and atomic number 2. It is a
        colorless, odorless, tasteless, non-toxic, inert, monatomic gas, the first in the noble gas
        group in the periodic table. Its boiling point is the lowest among all the elements.`,
  },
  {
    position: 3,
    name: 'Lithium',
    weight: 6.941,
    symbol: 'Li',
    description: `Lithium is a chemical element with symbol Li and atomic number 3. It is a soft,
        silvery-white alkali metal. Under standard conditions, it is the lightest metal and the
        lightest solid element.`,
  },
  {
    position: 4,
    name: 'Beryllium',
    weight: 9.0122,
    symbol: 'Be',
    description: `Beryllium is a chemical element with symbol Be and atomic number 4. It is a
        relatively rare element in the universe, usually occurring as a product of the spallation of
        larger atomic nuclei that have collided with cosmic rays.`,
  },
  {
    position: 5,
    name: 'Boron',
    weight: 10.811,
    symbol: 'B',
    description: `Boron is a chemical element with symbol B and atomic number 5. Produced entirely
        by cosmic ray spallation and supernovae and not by stellar nucleosynthesis, it is a
        low-abundance element in the Solar system and in the Earth's crust.`,
  },
  {
    position: 6,
    name: 'Carbon',
    weight: 12.0107,
    symbol: 'C',
    description: `Carbon is a chemical element with symbol C and atomic number 6. It is nonmetallic
        and tetravalent—making four electrons available to form covalent chemical bonds. It belongs
        to group 14 of the periodic table.`,
  },
  {
    position: 7,
    name: 'Nitrogen',
    weight: 14.0067,
    symbol: 'N',
    description: `Nitrogen is a chemical element with symbol N and atomic number 7. It was first
        discovered and isolated by Scottish physician Daniel Rutherford in 1772.`,
  },
  {
    position: 8,
    name: 'Oxygen',
    weight: 15.9994,
    symbol: 'O',
    description: `Oxygen is a chemical element with symbol O and atomic number 8. It is a member of
         the chalcogen group on the periodic table, a highly reactive nonmetal, and an oxidizing
         agent that readily forms oxides with most elements as well as with other compounds.`,
  },
  {
    position: 9,
    name: 'Fluorine',
    weight: 18.9984,
    symbol: 'F',
    description: `Fluorine is a chemical element with symbol F and atomic number 9. It is the
        lightest halogen and exists as a highly toxic pale yellow diatomic gas at standard
        conditions.`,
  },
  {
    position: 10,
    name: 'Neon',
    weight: 20.1797,
    symbol: 'Ne',
    description: `Neon is a chemical element with symbol Ne and atomic number 10. It is a noble gas.
        Neon is a colorless, odorless, inert monatomic gas under standard conditions, with about
        two-thirds the density of air.`,
  },
];