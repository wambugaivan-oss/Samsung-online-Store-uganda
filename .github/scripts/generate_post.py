      - name: Run Trend Script
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: |
          cd $GITHUB_WORKSPACE
          python .github/scripts/generate_post.py
