
from flask import Blueprint, render_template, request, url_for, Response, redirect, flash, current_app, jsonify
from flask_login import current_user, login_required
from werkzeug.exceptions import NotFound, BadRequest, RequestEntityTooLarge, InternalServerError
from datetime import datetime
from time import time
from listenbrainz import webserver
from listenbrainz.webserver import flash
import listenbrainz.db.user as db_user
import listenbrainz.config as config
from listenbrainz.db.exceptions import DatabaseException
from flask import make_response
from listenbrainz.webserver.login import User
from listenbrainz.webserver.redis_connection import _redis
import ujson
import os

spotify_bp = Blueprint("spotify", __name__)


@spotify_bp.route("/")
@login_required
def spotify():
    if request.method == "POST":
        return redirect(url_for("user.import_data"))
    else:
        return render_template(
            "spotify/index.html",
            user=current_user
        )
