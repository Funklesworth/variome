import React from 'react';

import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';


export default function References() {
    const referencesList = [
        {
            ref: 'dbSNP',
            val: 'rs7164960',
        },
        {
            ref: 'UCSC',
            val: 'Search UCSC',
        },
        {
            ref: 'Ensembl',
            val: 'Search Ensembl',
        },
        {
            ref: 'ClinVar',
            val: 'Search ClinVar',
        },
        {
            ref: 'gnomAD',
            val: 'Search gnomAD',
        }
    ]

    return (
        <React.Fragment>
            <Card>
                <CardContent>
                    <Grid container>
                        <Grid item xs={12}>
                            <Typography variant="h4" sx={{ fontWeight: 'light', paddingBottom: '5%' }}>
                                References
                            </Typography>
                        </Grid>
                        {referencesList.map((item, index) => (
                            <Grid container>
                                <Grid item xs={3} key={index}>
                                    <Typography variant="subtitle2" sx={{ fontWeight: 'bold' }}>
                                        {item.ref}
                                    </Typography>
                                </Grid>
                                <Grid item xs={9}>
                                    <Typography variant="subtitle1">
                                        {item.val}
                                    </Typography>
                                </Grid>
                            </Grid>
                        ))}
                    </Grid>
                </CardContent>
            </Card>
        </React.Fragment>
    )
}