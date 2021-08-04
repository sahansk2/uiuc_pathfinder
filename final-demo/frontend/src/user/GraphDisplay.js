import { getGraph,  mockReturnDataPrereqsCS225 as mockData, } from './util'
import CytoscapeComponent from 'react-cytoscapejs';
import cytoscape from 'cytoscape';
import cydagre from 'cytoscape-dagre'
import * as React from 'react';
import './user.css'

cytoscape.use(cydagre);

const ILLINI_BLUE = "#13294B";
const ILLINI_ORANGE = "#FF552E";

const graphComponentStyle = { 
    width: '100%', 
    height: '50vh', 
    border: "3px black solid",
    "selection-box-color": "slate"
}

const graphLayout = {
    name: 'dagre',
    fit: true,
    directed: true, 
    circle: true,
    refresh: 20
};

const graphStyleSheet = [
    {
        selector: "*",
        style: {
            "text-halign": "center",
            "text-valign": "center",
        }
    },
    {
        selector: "node",
        style: {
            label: "data(label)",
            "background-color": ILLINI_ORANGE, // Illini Orange
            "font-weight": "bold",
            "border-width": 12,
            "border-style": "solid",
            "border-color": "white",
            "border-opacity": 0
        }
    },
    {
        selector: "node:selected",
        style: {
            "overlay-color": "lime",
            "overlay-opacity": 0.2
        }
    },
    {
        selector: "edge",
        style: {
            "curve-style": 'bezier',
            "line-color": ILLINI_BLUE, // Illini Blue
            label: "data(label)",
            'target-arrow-color': ILLINI_BLUE,
            'target-arrow-shape': 'triangle',
            'arrow-scale': 1.5
        }
    },
    {
        selector: '[id ^= "OR_"]',
        style: {
            label: "data(label)",
            shape: "diamond",
            "font-size": 12,
            "background-color": "white",
            "border-width": 12,
            "border-color": "orange",
            "border-style": "solid",
            "overlay-opacity": 0
        }
    }
]

function MyCytoscape({ data: elements, cyRef }) {
    const prenodes = elements.nodes;
    const preedges = elements.edges;
    // We need to wrap this like this for cytoscape.
    
    React.useEffect(() => {
        if (cyRef.current !== null) {
            cyRef.current.layout(graphLayout).run()
        }
    })

    if (!prenodes || !preedges) {
        return <div> :( </div>
    }
    const cyNodes = prenodes.map(val => ({ 
        data: val 
    }) )
    const cyEdges = preedges.map(val => ({ data: val }) )

    const allElements = cyNodes.concat(cyEdges);



    return <CytoscapeComponent 
                id="cytoscapeGraph"
                elements={allElements}
                style={graphComponentStyle}
                stylesheet={graphStyleSheet}
                layout={graphLayout}
                cy={cy => {
                    cyRef.current = cy
                }}
                diff={() => true}/>
}


const GraphDisplay = ({ data }) => {
    const cyRef = React.useRef(null);
    return <div> {
        data && <React.Fragment>
            <div>
            <button onClick={() => {
                cyRef.current?.fit()
                cyRef.current?.layout(graphLayout).run()
            }}>Reset GraphDisplay</button>
        </div>
        <MyCytoscape data={data} cyRef={cyRef}/>
            </React.Fragment>
    }</div>
}

export {
    GraphDisplay
} 