import Ember from 'ember';
import SaveModelMixin from 'pi-ember/mixins/piLapsers/save-model-mixin';

export default Ember.Route.extend(SaveModelMixin, {
  model: function() {
    return this.store.createRecord('piLapser');
  }
});
