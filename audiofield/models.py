from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.db.models.signals import post_save
from django.conf import settings
from datetime import datetime, timedelta
from common.intermediate_model_base_class import Model
from audiofield.fields import AudioField
import os.path


# This Model describe the Audio used on the platform, this allow to upload audio file and configure alternate Text2Speech System
class AudioFile(Model):
    name = models.CharField(max_length=150, blank=False,
                            verbose_name="Audio Name",
                            help_text='Audio label')
    
    audio_file = AudioField(upload_to='upload/audiofiles', blank=True,
                            ext_whitelist=(".mp3", ".wav", ".ogg"))
    user = models.ForeignKey(User, verbose_name='User',
                             help_text=_("Select User"))
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = u'audio_file'
        verbose_name = _("Audio file")
        verbose_name_plural = _("Audio files")

    def __unicode__(self):
        return '[%s] %s' %(self.id, self.name)

    def save(self):
        #print "Before save"
        super(AudioFile, self).save() # Call the "real" save() method
        #print "After save"

    def audio_file_player(self):
        """audio player tag for admin"""
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.audio_file)
            player_string = '<ul class="playlist"><li style="width:250px;">\
            <a href="%s">%s</a></li></ul>' % (file_url, os.path.basename(file_url))
            return player_string
    audio_file_player.allow_tags = True
    audio_file_player.short_description = _('Audio file player')


