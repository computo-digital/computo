import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OperationalLocationClassAddComponent } from './operational-location-class-add.component';

describe('OperationalLocationClassAddComponent', () => {
  let component: OperationalLocationClassAddComponent;
  let fixture: ComponentFixture<OperationalLocationClassAddComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OperationalLocationClassAddComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OperationalLocationClassAddComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
