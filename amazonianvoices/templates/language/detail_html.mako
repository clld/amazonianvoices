<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "languages" %>
<%block name="title">${_('Language')} ${ctx.name}</%block>

<h2>${_('Language')} ${ctx.name}</h2>


<div class="tabbable" style="clear: both">
    <ul class="nav nav-tabs">
        <li class="active"><a href="#words" data-toggle="tab">${_('Values')}</a></li>
        <li><a href="#ipa" data-toggle="tab">${_('Sound Inventory')}</a></li>
    </ul>
    <div class="tab-content" style="overflow: scroll;">
        <div id="words" class="tab-pane active">
            ${request.get_datatable('values', h.models.Value, language=ctx).render()}
        </div>
        <div id="ipa" class="tab-pane">
            ${consonants_html|n}
            ${vowels_html|n}

            <table class="table table-condensed table-nonfluid">
                <caption>${_('Other phonemes')}</caption>
                <tbody>
                    % for seg in uncovered:
                        % if seg.sound_bipa != '+':
                            <tr>
                                <th>${seg.sound_bipa}</th>
                                <td>${seg.sound_name}</td>
                            </tr>
                        % endif
                    % endfor
                </tbody>
            </table>
        </div>
    </div>
    <script>
        $(document).ready(function () {
            if (location.hash !== '') {
                $('a[href="#' + location.hash.substr(2) + '"]').tab('show');
            }
            return $('a[data-toggle="tab"]').on('shown', function (e) {
                return location.hash = 't' + $(e.target).attr('href').substr(1);
            });
        });
    </script>
</div>


<%def name="sidebar()">
    ${util.codes(ctx)}
    % if ctx.contribution.contributor_assocs:
        <h4>${_('Contributors')}</h4>
        <ul class="unstyled">
            % for ca in ctx.contribution.contributor_assocs:
                <li>
                    <strong>${ca.contributor.name}</strong>: ${', '.join([r.replace('_', ' ') for r in ca.jsondata['roles']])}
                </li>
            % endfor
        </ul>
    % endif
    % if ctx.family:
        <strong>${_('Family')}</strong>: ${ctx.family}
    % endif
    ${util.language_meta()}
</%def>
