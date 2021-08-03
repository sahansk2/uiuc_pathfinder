import { getGraph,  mockReturnDataPrereqsCS225 as mockData, } from './util'
import CytoscapeComponent from 'react-cytoscapejs';
import cytoscape from 'cytoscape';
import cydagre from 'cytoscape-dagre'
import * as React from 'react';
import './user.css'

cytoscape.use(cydagre);

function MyCytoscape(props) {
    const elements = getGraph(mockData);
    const prenodes = elements.nodes;
    const preedges = elements.edges;
    const cyNodes = prenodes.map(val => {
        return {
            data: val
        }
    })
    const cyEdges = preedges.map(val => {
        return {
            data: val
        }
    })

    
    return <CytoscapeComponent elements={CytoscapeComponent.normalizeElements(cyNodes.concat(cyEdges))}
        style={ { width: '600px', height: '600px' } }
                layout={{name: 'dagre',
            directed: true,
        circle: true}}/>
}


    
const onClickNode = (id) => {
    console.log("Clicked node with id=", id)
}

const GraphDisplay = () => {
    const data = getGraph(mockData);
    return <div>
        <MyCytoscape/>
    </div>
}

export {
    GraphDisplay
} 