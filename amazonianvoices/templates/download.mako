<%inherit file="home_comp.mako"/>
<%namespace name="mpg" file="clldmpg_util.mako"/>

<h3>${_('Downloads')}</h3>

<div class="alert alert-info">
    <p>
        ${_('Amazonian Voices serves the latest')}
        ${h.external_link('https://github.com/lexibank/amazonianvoices/releases', label=_('released version'))}
        ${_('of data curated at')}
        ${h.external_link('https://github.com/lexibank/amazonianvoices', label='lexibank/amazonianvoices')}.
        ${_('All released version are accessible via')} <br/>
        <br/>
        ${_('on ZENODO as well')}.
    </p>
</div>
