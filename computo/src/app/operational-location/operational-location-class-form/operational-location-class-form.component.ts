import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'app-operational-location-class-form',
  templateUrl: './operational-location-class-form.component.html',
  styleUrls: ['./operational-location-class-form.component.css']
})
export class OperationalLocationClassFormComponent implements OnInit {

  public id: string | null = null;

  constructor(
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
    });
  }

}
