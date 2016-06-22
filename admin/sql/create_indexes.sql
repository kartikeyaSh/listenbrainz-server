BEGIN;

CREATE UNIQUE INDEX auth_token_ndx_user ON "user" (auth_token);
CREATE UNIQUE INDEX lower_musicbrainz_id_ndx_user ON "user" (lower(musicbrainz_id));

CREATE UNIQUE INDEX user_id_ts_ndx_listens ON "listens" (user_id, ts);
CREATE INDEX user_id_ndx_listens ON "listens" (user_id);
CREATE INDEX ts_ndx_listens ON "listens" (ts);

COMMIT;
