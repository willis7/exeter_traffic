node {
    def PYTHON_VERSION = "3.5"
    def CONDA_VERSION = "4.1.11"
    stage 'setup'

        // Download the miniconda tool
        sh "curl https://repo.continuum.io/miniconda/Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh -o miniconda.sh"

        // Make the tool executable
        sh 'chmod +x ./miniconda.sh'

        // Run setup
        sh './miniconda.sh -b -p /miniconda'

        // Make conda available to the command line
        env.PATH = "/miniconda/bin:${env.PATH}"

        // Get the latest code
        checkout scm

        // Setup conda
        sh 'hash -r'
        sh 'conda config --set always_yes yes --set changeps1 no'
        sh 'conda update -q conda'
        sh 'conda info -a'

    stage 'build'
        // We need to configure a virtual display
        sh 'apt-get install -y xvfb'
        env.DISPLAY=":99"
        sh 'Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &'

        // Set up the runtime environment
        sh 'conda env create -f environment.yml'
        sh '''. activate exeter_traffic
            cd scripts
            python make_relative_csv.py'''

        // Run the jobs in parallel to improve build times
        parallel (
             map1: { sh '''. activate exeter_traffic
                        cd scripts
                        python plot_relative_maps.py''' },
             map2: { sh '''. activate exeter_traffic
                        cd scripts
                        python plot_color_maps.py''' },
             map3: { sh '''. activate exeter_traffic
                        cd scripts
                        python plot_timeseries.py''' },
             map4: { sh '''. activate exeter_traffic
                        cd scripts
                        python plot_barplots.py''' }
           )

    stage 'lint'
        // We know this has the potential to fail, so we wrap it in a catchError block.
        // Doing this allows us to proceed to the archive task
        catchError {
            sh "conda create -q -n test-environment python=${PYTHON_VERSION} pylint"
            sh '''. activate test-environment
                pylint scripts --output-format=html > lint.html'''
        }

        publishHTML([allowMissing: true, alwaysLinkToLastBuild: false, keepAll: true, reportDir: '', reportFiles: 'lint.html', reportName: 'Linting Report'])

    stage 'archive'
      archiveArtifacts artifacts: 'plots/barplots/**/*.png,plots/maps/**/*.png,plots/tseries/*.png', caseSensitive: false, fingerprint: true
}
