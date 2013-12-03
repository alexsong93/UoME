# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'UoMeApp_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=40)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'UoMeApp', ['Event'])

        # Adding model 'UoMePost'
        db.create_table(u'UoMeApp_uomepost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=40)),
        ))
        db.send_create_signal(u'UoMeApp', ['UoMePost'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'UoMeApp_event')

        # Deleting model 'UoMePost'
        db.delete_table(u'UoMeApp_uomepost')


    models = {
        u'UoMeApp.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'UoMeApp.uomepost': {
            'Meta': {'object_name': 'UoMePost'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'})
        }
    }

    complete_apps = ['UoMeApp']