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


<div id="with-background">
    <h2>${_('Welcome to')} Amazonian Voices</h2>

    <p class="lead">
        ${_('Amazonian Voices presents phonetically-transcribed primary recordings.')}
    </p>

    <p>
        ${_('Cite the Amazonian Voices dataset as')}
    </p>
    <blockquote>
        
    </blockquote>
</div>
