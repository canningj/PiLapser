import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('piLapsers', function() {
    this.route('new');

    this.route('edit', {
      path: ':piLapser_id/edit'
    });

    this.route('show', {
      path: ':piLapser_id'
    });
  });
  this.route('createTL');
});

export default Router;
