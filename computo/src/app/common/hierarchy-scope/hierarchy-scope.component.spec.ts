import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HierarchyScopeComponent } from './hierarchy-scope.component';

describe('HierarchyScopeComponent', () => {
  let component: HierarchyScopeComponent;
  let fixture: ComponentFixture<HierarchyScopeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HierarchyScopeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HierarchyScopeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
