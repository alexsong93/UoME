# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UoMePost.event'
        db.add_column(u'UoMeApp_uomepost', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['UoMeApp.Event']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UoMePost.event'
        db.delete_column(u'UoMeApp_uomepost', 'event_id')


    models = {
        u'UoMeApp.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'UoMeApp.uomepost': {
            'Meta': {'ordering': "['pub_date']", 'object_name': 'UoMePost'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['UoMeApp.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'})
        }
    }

    complete_apps = ['UoMeApp']