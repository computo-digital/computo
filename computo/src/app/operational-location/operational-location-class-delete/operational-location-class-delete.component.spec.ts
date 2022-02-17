import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OperationalLocationClassDeleteComponent } from './operational-location-class-delete.component';

describe('OperationalLocationClassDeleteComponent', () => {
  let component: OperationalLocationClassDeleteComponent;
  let fixture: ComponentFixture<OperationalLocationClassDeleteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OperationalLocationClassDeleteComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OperationalLocationClassDeleteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
