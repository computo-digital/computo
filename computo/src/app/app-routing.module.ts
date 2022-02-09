import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OperationalLocationComponent } from './operational-location/operational-location/operational-location.component';
import { OperationalLocationClassListComponent } from './operational-location/operational-location-class-list/operational-location-class-list.component';
import { OperationalLocationClassFormComponent } from './operational-location/operational-location-class-form/operational-location-class-form.component';

const routes: Routes = [
  {
    path: 'operational/location',
    component: OperationalLocationComponent
  },
  {
  path: 'operational/location/class',
  component: OperationalLocationClassListComponent
  },
  {
    path: 'operational/location/class/:id',
    component: OperationalLocationClassFormComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
