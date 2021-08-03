import * as React from 'react';

import {GraphDisplay} from './GraphDisplay'

function UserDashboard(props) {
    return <div>
        <div>
            <input type="radio" name="searchmode" value="prereqs"/>Prereqs<br/>
            <input type="radio" name="searchmode" value="reverse"/>Dependents<br/>
        </div>
        <GraphDisplay/>
    </div>
}

export {
    UserDashboard
}
