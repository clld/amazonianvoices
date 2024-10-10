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
    <div style="float:left;margin:10px;margin-top:60px">
        <h4>${_('Statistics')}</h4>
        <table class="table table-condensed">
            <tbody>
            <tr>
                <th>${_('Languages')}</th>
                <td class="right">${'{:,}'.format(stats['language'])}</td>
            </tr>
            <tr>
                <th>${_('Parameters')}</th>
                <td class="right">${'{:,}'.format(stats['parameter'])}</td>
            </tr>
            <tr>
                <th>${_('Values')}</th>
                <td class="right">${'{:,}'.format(stats['value'])}</td>
            </tr>
            </tbody>
        </table>
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
