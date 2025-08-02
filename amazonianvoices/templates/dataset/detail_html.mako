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
    <img src="${req.static_url('amazonianvoices:static/Amazon_Voices_negro.png')}" width=150 alt="Logo"/>
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
        Alonso Vásquez-Aguilar, Roberto Zariquiey, Mariana Poblete, Hans-Jörg Bibiko, Raquel Cabrera, Minerva Cerna, Jorge Pérez Silva, Robert Forkel, Russell Gray.
        (2025) Amazonian Voices.
    </blockquote>
</div>
