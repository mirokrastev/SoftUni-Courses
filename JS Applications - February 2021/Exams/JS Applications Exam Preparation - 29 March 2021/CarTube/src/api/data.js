export function FormDataPairs(formData, ...exclude) {
    exclude = exclude || [];
    const data = [...formData.entries()]
        .reduce((p, [k, v]) => Object.assign(p, {[k]: v}), {});

    exclude.forEach(e => {
        if (data.hasOwnProperty(e))
            delete data[e];
    });
    return data;
}

