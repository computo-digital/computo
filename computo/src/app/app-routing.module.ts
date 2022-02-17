import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OperationalLocationClassAddComponent } from './operational-location/operational-location-class-add/operational-location-class-add.component';
import { OperationalLocationClassDeleteComponent } from './operational-location/operational-location-class-delete/operational-location-class-delete.component';
import { OperationalLocationClassListComponent } from './operational-location/operational-location-class-list/operational-location-class-list.component';
import { OperationalLocationClassUpdateComponent } from './operational-location/operational-location-class-update/operational-location-class-update.component';
import { OperationalLocationComponent } from './operational-location/operational-location/operational-location.component';

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
    path: 'operational/location/class/add',
    component: OperationalLocationClassAddComponent
  },
  {
    path: 'operational/location/class/update/:id',
    component: OperationalLocationClassUpdateComponent
  },
  {
    path: 'operational/location/class/delete/:id',
    component: OperationalLocationClassDeleteComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
