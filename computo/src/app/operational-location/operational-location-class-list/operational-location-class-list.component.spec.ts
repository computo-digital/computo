import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OperationalLocationClassListComponent } from './operational-location-class-list.component';

describe('OperationalLocationClassListComponent', () => {
  let component: OperationalLocationClassListComponent;
  let fixture: ComponentFixture<OperationalLocationClassListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OperationalLocationClassListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OperationalLocationClassListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
