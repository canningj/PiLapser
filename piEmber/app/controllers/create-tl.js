import Ember from 'ember';
import ENV from 'piEmber/config/environment';

export default Ember.Controller.extend({

  move_pos() {
      Ember.$.ajax({
        url: 'localhost:8000//move_pos/',
        type: 'POST',
      });
    },

  actions: {
    runTimelapse() {
      let {total_images, length, interval, shutter_speed, direction} = this.getProperties(
        'total_images',
        'length',
        'interval',
        'shutter_speed',
        'direction'
      );

      Ember.$.ajax({
        url: ENV.host + '/run_timelapse/',
        type: 'POST',
        data: {
          total_images: total_images,
          length: length,
          interval: interval,
          shutter_speed: shutter_speed,
          direction: direction
        },
      });
    },

    move_pos() {
      Ember.$.ajax({
        url: 'localhost:8000//move_pos/',
        type: 'POST',
      });
    },

    move_neg() {
      Ember.$.ajax({
        url: 'localhost:8000//move_neg/',
        type: 'POST',
      });
    }
  }
});
