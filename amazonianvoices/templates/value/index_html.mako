<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "values" %>
<%block name="title">${_('Values')}</%block>


<h2>${_('Values')}</h2>
<div>
    ${ctx.render()}
</div>
