import DS from 'ember-data';

export default DS.Model.extend({
  totalImages: DS.attr('integer'),
  length: DS.attr('integer'),
  interval: DS.attr('integer'),
  shutterSpeed: DS.attr('integer'),
  direction: DS.attr('char')
});
