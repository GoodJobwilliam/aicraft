import io
import json

from scripts.distribution_report import DistributionSnapshot, fetch_snapshot, report


class Response:
    def __init__(self, payload):
        self.payload = io.StringIO(json.dumps(payload))

    def __enter__(self):
        return self.payload

    def __exit__(self, *_args):
        self.payload.close()


def test_fetch_snapshot_reads_pypi_and_release_assets():
    def opener(request, timeout):
        assert timeout == 20
        if "pypistats.org" in request.full_url:
            return Response({"data": {"last_day": 2, "last_week": 33, "last_month": 352}})
        return Response({"assets": [{"name": "mcp-code-review-trial.zip", "download_count": 4}]})

    snapshot = fetch_snapshot(opener=opener)

    assert snapshot == DistributionSnapshot(2, 33, 352, {"mcp-code-review-trial.zip": 4})


def test_report_labels_downloads_as_non_revenue():
    output = report(DistributionSnapshot(2, 33, 352, {"bundle.zip": 4}))
    assert "last 30 days): 352" in output
    assert "bundle.zip: 4" in output
    assert "not contacts, trials, customers, or revenue" in output
