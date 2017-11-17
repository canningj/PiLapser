import Ember from 'ember';
import { module, test } from 'qunit';
import startApp from '../helpers/start-app';

var application;
var originalConfirm;
var confirmCalledWith;

module('Acceptance: PiLapser', {
  beforeEach: function() {
    application = startApp();
    originalConfirm = window.confirm;
    window.confirm = function() {
      confirmCalledWith = [].slice.call(arguments);
      return true;
    };
  },
  afterEach: function() {
    Ember.run(application, 'destroy');
    window.confirm = originalConfirm;
    confirmCalledWith = null;
  }
});

test('visiting /piLapsers without data', function(assert) {
  visit('/piLapsers');

  andThen(function() {
    assert.equal(currentPath(), 'piLapsers.index');
    assert.equal(find('#blankslate').text().trim(), 'No Pilapsers found');
  });
});

test('visiting /piLapsers with data', function(assert) {
  server.create('piLapser');
  visit('/piLapsers');

  andThen(function() {
    assert.equal(currentPath(), 'piLapsers.index');
    assert.equal(find('#blankslate').length, 0);
    assert.equal(find('table tbody tr').length, 1);
  });
});

test('create a new piLapser', function(assert) {
  visit('/piLapsers');
  click('a:contains(New Pilapser)');

  andThen(function() {
    assert.equal(currentPath(), 'piLapsers.new');

    fillIn('label:contains(Totalimages) input', 'MyString');
    fillIn('label:contains(Length) input', 'MyString');
    fillIn('label:contains(Interval) input', 'MyString');
    fillIn('label:contains(Shutter speed) input', 'MyString');
    fillIn('label:contains(Direction) input', 'MyString');

    click('input:submit');
  });

  andThen(function() {
    assert.equal(find('#blankslate').length, 0);
    assert.equal(find('table tbody tr').length, 1);
  });
});

test('update an existing piLapser', function(assert) {
  server.create('piLapser');
  visit('/piLapsers');
  click('a:contains(Edit)');

  andThen(function() {
    assert.equal(currentPath(), 'piLapsers.edit');

    fillIn('label:contains(Totalimages) input', 'MyString');
    fillIn('label:contains(Length) input', 'MyString');
    fillIn('label:contains(Interval) input', 'MyString');
    fillIn('label:contains(Shutter speed) input', 'MyString');
    fillIn('label:contains(Direction) input', 'MyString');

    click('input:submit');
  });

  andThen(function() {
    assert.equal(find('#blankslate').length, 0);
    assert.equal(find('table tbody tr').length, 1);
  });
});

test('show an existing piLapser', function(assert) {
  server.create('piLapser');
  visit('/piLapsers');
  click('a:contains(Show)');

  andThen(function() {
    assert.equal(currentPath(), 'piLapsers.show');

    assert.equal(find('p strong:contains(Totalimages:)').next().text(), 'MyString');
    assert.equal(find('p strong:contains(Length:)').next().text(), 'MyString');
    assert.equal(find('p strong:contains(Interval:)').next().text(), 'MyString');
    assert.equal(find('p strong:contains(Shutter speed:)').next().text(), 'MyString');
    assert.equal(find('p strong:contains(Direction:)').next().text(), 'MyString');
  });
});

test('delete a piLapser', function(assert) {
  server.create('piLapser');
  visit('/piLapsers');
  click('a:contains(Remove)');

  andThen(function() {
    assert.equal(currentPath(), 'piLapsers.index');
    assert.deepEqual(confirmCalledWith, ['Are you sure?']);
    assert.equal(find('#blankslate').length, 1);
  });
});
