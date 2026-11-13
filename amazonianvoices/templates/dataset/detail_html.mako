<%inherit file="../home_comp.mako"/>

<%block name="head">
    <style>
        .dt-before-table {visibility: hidden; height: 0;}
        .dataTables_info {visibility: hidden; height: 0;}
        .dataTables_paginate {visibility: hidden; height: 0;}
    </style>
</%block>

<%def name="sidebar()">
    <div class="well">
        <img src="${req.static_url('amazonianvoices:static/ico-AmazonianVoices.jpg')}" class="img-rounded">
    </div>
</%def>


<div style="float:left;margin-top:10px; margin-right: 1em;">
    <img src="${req.static_url('amazonianvoices:static/Amazonian_voices_logo.svg')}" width=200 alt="Logo"/>
</div>

<div id="with-background">
    <h2>${_('Welcome to')} Amazonian Voices</h2>

    <p class="lead">
        ${_('Amazonian Voices presents phonetically-transcribed primary recordings.')}
    </p>

    <p style="clear: left">
        ${_('Cite the Amazonian Voices dataset as')}
    </p>
    <blockquote>
Alonso Vásquez, Roberto Zariquiey, Mariana Poblete, Hans-Jörg Bibiko, Frederic Blum, Raquel Cabrera, Minerva Cerna, Jorge Pérez Silva, Robert Forkel, & Russell Gray. (2026). Amazonian Voices (Version v1.0) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.23467623
    </blockquote>
</div>
